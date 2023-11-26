<script setup>
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
</script>

<script>
export default {
  data: () => ({
    stickySplitLabelsEnabled: true,
    minCellWidth: 0,
    appointmentsFromDatabase: [],
    minSplitWidth: 0,
    splitDays: [
      // The id property is added automatically if none (starting from 1), but you can set a custom one.
      // If you need to toggle the splits, you must set the id explicitly.
      { id: 1, class: "tb1", label: "TB1", hide: false },
      { id: 2, class: "tb2", label: "TB2", hide: false },
      { id: 3, class: "vb1", label: "VB1", hide: false },
      { id: 4, class: "vb2", label: "VB2", hide: false },
      { id: 5, class: "u", label: "U1", hide: false },
    ],
    draggables: [
      {
        // The id (or however you name it), will help you find which event to delete
        // from the callback triggered on drop into Vue Cal.
        id: 1,
        title: "Planned Maintenance",
        duration: 60,
        class: "closed"
      },
      {
        id: 2,
        title: "Planned Maintenance",
        duration: 30,
        class: "closed"
      },
      {
        id: 3,
        title: "Planned Maintenance",
        // No defined duration here: will default to 2 hours.
        class: "closed"
      },
    ],
  }),
  mounted() {
    this.fetchEntriesFromDatabase()
  },
  methods: {
    determineSplit(machine_id) {
      return this.splitDays.find(d => {
        return machine_id == d.label
      }).id
    },
    fetchEntriesFromDatabase() {
        fetch(`http://127.0.0.1:8000/api/v1/appointment?nested=true`).then((response) => {
            response.json().then((data) => {
                if (response.ok) {
                    const appointmentsFromDatabase = data.map(d => {
                      return {
                          start: new Date(d.start_time),
                          end: new Date(d.end_time),
                          title: d.machine.machine_name,
                          content: `[${d.priority.name}] ${d.patient.first_name} ${d.patient.last_name}`,
                          class: "health",
                          appointment: d,
                          split: this.determineSplit(d.machine.id), // Has to match the id of the split you have set (or integers if none).
                        }
                    })
                    fetch(`http://127.0.0.1:8000/api/v1/maintenance?nested=true`).then((response) => {
                        response.json().then((data) => {
                            if (response.ok) {
                                console.log(data)
                                const maintenancesFromDatabase = data.map(d => {
                                  return {
                                      start: new Date(d.start_time),
                                      end: new Date(d.end_time),
                                      title: d.machine.machine_name,
                                      content: `${d.machine.machine_name}`,
                                      class: "maintenance",
                                      appointment: d,
                                      split: this.determineSplit(d.machine.id), // Has to match the id of the split you have set (or integers if none).
                                    }
                                })

                                this.appointmentsFromDatabase = [...maintenancesFromDatabase,
                                                                 ...appointmentsFromDatabase]
                            }
                        })
                    })

                }
            })
        })
    },
    formatDateForDatabase(unformatted) {
      const date = new Date(unformatted)
      const year = date.getFullYear()
      let month = date.getMonth() + 1
      let day = date.getDate()
      let hours = date.getHours()
      let minutes = date.getMinutes()
      let seconds = date.getSeconds()

      month = this.placeZeroInFrontIfLessThan10(month)
      day = this.placeZeroInFrontIfLessThan10(day)
      hours = this.placeZeroInFrontIfLessThan10(hours)
      minutes = this.placeZeroInFrontIfLessThan10(minutes)
      seconds = this.placeZeroInFrontIfLessThan10(seconds)

      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
    },
    placeZeroInFrontIfLessThan10(value) {
        if (parseInt(value) < 10 && parseInt(value) >= 0 && String(value).length == 1) {
            value = '0' + value
        }
        return value
    },
    onEventChange(e) {
      const new_start_time = this.formatDateForDatabase(e.event.start)
      const new_end_time = this.formatDateForDatabase(e.event.end)

      if (e.event.appointment) {
        fetch(`http://127.0.0.1:8000/api/v1/appointment?id=${e.event.appointment.id}&nested=false`)
        .then((get_response) => {
          get_response.json().then((appointment) => {
            // Update start and end times
            appointment.start_time = new_start_time
            appointment.end_time = new_end_time
            fetch('http://127.0.0.1:8000/api/v1/appointment', {
              method: 'PUT',
              headers: {
                'Content-type': 'application/json'
              },
              body: JSON.stringify(appointment)
            }).then((response) => {
              response.json().then((data) => {
                this.fetchEntriesFromDatabase()
              })
            })
          })
        })
      }
    },
    onEventDragStart(e, draggable) {
      // Passing the event's data to Vue Cal through the DataTransfer object.
      e.dataTransfer.setData("event", JSON.stringify(draggable));
      e.dataTransfer.setData("cursor-grab-at", e.offsetY);
    },
    // The 3 parameters are destructured from the passed $event in @event-drop="onEventDrop".
    // `event` is the final event as Vue Cal understands it.
    // `originalEvent` is the event that was dragged into Vue Cal, it can come from the same
    //  Vue Cal instance, another one, or an external source.
    // `external` is a boolean that lets you know if the event is not coming from any Vue Cal.
    onEventDrop({ event, originalEvent, external }) {
      // If the event is external, delete it from the data source on drop into Vue Cal.
      // If the event comes from another Vue Cal instance, it will be deleted automatically in there.
      if (external) {
        const extEventToDeletePos = this.draggables.findIndex(
          (item) => item.id === originalEvent.id
        );
        if (extEventToDeletePos > -1)
          this.draggables.splice(extEventToDeletePos, 1);
      }
    },
  },
};

/* // Special hours */
/* const overTime = { from: 17 * 60, to: 20 * 60, class: 'overtime-hours' }; */
/* // In your component's data, special hours from Monday to Friday. */
/* // Note that you can provide an array of multiple blocks for the same day. */
/* : { */
/*   1: overTime */
/* }; */
</script>

<template>
  <main class="container">
    <div class="container">
      <div
        class="row align-items-center"
        style="display: flex; align-items: center; justify-content: center"
      >
        <div
          style="display: flex; align-items: center; justify-content: center"
        >
          <img
            alt="Team icon"
            src="./assets/icon.jpg"
            class="img-fluid"
            style="max-width: 60px; max-height: 60px"
          />
        </div>
        <div
          style="display: flex; align-items: center; justify-content: center"
        >
          <h4>A near-smart scheduler</h4>
        </div>
      </div>
    </div>
    <br />

    <div class="row align-items-start">
      <div class="patient-rack col d-none d-lg-block">
        <!-- WIP: add patient -->
        <br />
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            value=""
            id="flexCheckChecked"
            @click="minCellWidth = minCellWidth ? 0 : 400"
          />
          <label class="form-check-label" for="flexCheckChecked">
            Expand day column
          </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            value=""
            id="flexCheckChecked"
            @click="minSplitWidth = minSplitWidth ? 0 : 200"
          />
          <label class="form-check-label" for="flexCheckChecked">
            Expand machine column
          </label>
        </div>
        <br /><br />
        <div>
          <button
            type="button"
            class="btn btn-primary"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
          >
            Add patient
          </button>

          <div
            class="modal fade"
            id="exampleModal"
            tabindex="-1"
            aria-labelledby="exampleModalLabel"
            aria-hidden="true"
          >
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLabel">
                    Patient Info
                  </h5>
                  <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                  ></button>
                </div>
                <div class="modal-body">
                  <form>
                    <div class="mb-3">
                      <label class="col-form-label">First name:</label>
                      <input type="text" class="form-control" />
                    </div>
                    <div class="mb-3">
                      <label class="col-form-label">Last name:</label>
                      <input type="text" class="form-control" />
                    </div>
                    <div class="mb-3">
                      <label class="col-form-label">Duration:</label>
                      <input type="text" class="form-control" />
                    </div>
                    <div class="mb-3">
                      <label class="col-form-label">Organ:</label>
                      <input type="text" class="form-control" />
                    </div>
                  </form>
                </div>
                <div class="modal-footer">
                  <button
                    type="button"
                    class="btn btn-secondary"
                    data-bs-dismiss="modal"
                  >
                    Close
                  </button>
                  <button type="button" class="btn btn-primary">Submit</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <br />
        <!-- WIP: patient card list -->
        <!-- Three HTML5 draggable events. -->

        <div
          class="external-event card"
          style="margin: 1%"
          v-for="(item, i) in draggables"
          :key="i"
          draggable="true"
          @dragstart="onEventDragStart($event, item)"
        >
          <div class="row">
            <div class="col">
              <strong>{{ item.title }}</strong>
              ({{ item.duration ? `${item.duration} min` : "no duration" }})
              <div>{{ item.content }}</div>
            </div>
            <div class="col">
              <!-- Button trigger modal -->
              <button
                type="button"
                class="btn btn-outline-primary"
                data-bs-toggle="modal"
                data-bs-target="#staticBackdrop"
              >
                Details
              </button>
              <!-- Modal -->
              <div
                class="modal fade"
                id="staticBackdrop"
                data-bs-backdrop="static"
                data-bs-keyboard="false"
                tabindex="-1"
                aria-labelledby="staticBackdropLabel"
                aria-hidden="true"
              >
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title" id="staticBackdropLabel">
                        Time-slot details
                      </h5>
                      <button
                        type="button"
                        class="btn-close"
                        data-bs-dismiss="modal"
                        aria-label="Close"
                      ></button>
                    </div>
                    <div class="modal-body">
                      <p>Patient Info</p>
                      <p>Treatment Info</p>
                    </div>
                    <div class="modal-footer">
                      <button
                        type="button"
                        class="btn btn-secondary"
                        data-bs-dismiss="modal"
                      >
                        Close
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <br />
        <button type="button" class="btn btn-primary">
          Assign automatically
        </button>
      </div>

      <div class="calendar col-10">
        <!-- For loop for splitDays[i] -->
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            value=""
            id="flexCheckChecked"
            checked
            @click="splitDays[0].hide = !splitDays[0].hide"
          />
          <label class="form-check-label" for="flexCheckChecked">
            Show TB1
          </label>
        </div>

        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            value=""
            id="flexCheckChecked"
            checked
            @click="splitDays[1].hide = !splitDays[1].hide"
          />
          <label class="form-check-label" for="flexCheckChecked">
            Show TB2
          </label>
        </div>

        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            value=""
            id="flexCheckChecked"
            checked
            @click="splitDays[2].hide = !splitDays[2].hide"
          />
          <label class="form-check-label" for="flexCheckChecked">
            Show VB1
          </label>
        </div>

        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            value=""
            id="flexCheckChecked"
            checked
            @click="splitDays[3].hide = !splitDays[3].hide"
          />
          <label class="form-check-label" for="flexCheckChecked">
            Show VB2
          </label>
        </div>

        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            value=""
            id="flexCheckChecked"
            checked
            @click="splitDays[4].hide = !splitDays[4].hide"
          />
          <label class="form-check-label" for="flexCheckChecked">
            Show U
          </label>
        </div>

        <vue-cal
          :special-hours="specialHours"
          hide-weekends
          :disable-views="['years', 'year']"
          :min-cell-width="minCellWidth"
          :min-split-width="minSplitWidth"
          :sticky-split-labels="stickySplitLabelsEnabled"
          :time-from="8 * 60"
          :time-to="18 * 60"
          :time-step="15"
          :snap-to-time="15"
          :events="appointmentsFromDatabase"
          :editable-events="{
            title: false,
            drag: true,
            resize: false,
            delete: true,
            create: false,
          }"
          @event-drop="onEventDrop"
          :split-days="splitDays"
          selected-date="2023-11-27"
          @event-change="onEventChange"
        >
        </vue-cal>
      </div>
    </div>
  </main>
</template>

<style>
.row {
  display: flex;
  align-items: center;
  justify-content: center;
}

.col h2 {
  font-family: "Arial", sans-serif;
  color: #333; /* Adjust the color as needed */
}

.html {
  overflow: hidden;
  width: 100vh;
  height: 100vh;
  margin: 0% !important;
}
.container {
  max-width: 100% !important;
  padding: 2% !important;
}

.form-check-input:checked {
  background-color: #fb8500 !important;
  border-color: #fb8500 !important;
}

.btn-primary {
  background-color: #219ebc !important;
  border-color: #219ebc !important;
}
.btn-primary:hover {
  background-color: #023047 !important;
  border-color: #023047 !important;
}
.btn-outline-primary {
  --bs-btn-color: none;
  border-color: #023047 !important;
}
.btn-outline-primary:hover {
  color: #023047 !important;
  background-color: none !important;
}

.calendar {
  height: 100vh !important;
}
.vue-cal {
  padding: 1rem;
  height: 80vh;
}

.vuecal__title-bar {
  background-color: #ffb703 !important;
  font-size: 15px;
}
.vuecal__menu {
  background-color: #8ecae6 !important;
  font-size: 12px;
}
.vuecal__view-btn:hover {
  background: #023047 !important;
}
.vuecal__view-btn--active {
  background: #219ebc !important;
}

.vuecal__flex .vuecal__heading {
  border-left-style: dotted;
}

.vuecal__event {
  background-color: #ffb703 !important;
}

/* You can easily set a different style for each split of your days. */
.vuecal__cell-split.tb1 {
  background-color: #8ecae62e !important;
}
.vuecal__cell-split.tb2 {
  background-color: #219dbc2f !important;
}
.vuecal__cell-split.vb1 {
  background-color: #35835934 !important;
}
.vuecal__cell-split.vb2 {
  background-color: #ffb80321 !important;
}
.vuecal__cell-split.u {
  background-color: #f2aa1a30 !important;
}

.vuecal__event {
  box-shadow: 0px 2px 5px 0px #969696;
  border: 1px solid #d4d4d4;
  border-radius: 5px;
}

/* Different color for different event types. */
/* .vuecal__event.leisure {background-color: rgba(253, 156, 66, 0.9);border: 1px solid rgb(233, 136, 46);color: #fff;} */
/* .vuecal__event.health {background-color: rgba(164, 230, 210, 0.9);border: 1px solid rgb(144, 210, 190);} */
/* .vuecal__event.sport {background-color: rgba(255, 102, 102, 0.9);border: 1px solid rgb(235, 82, 82);color: #fff;} */

@media (max-width: 991.98px) {
  .main {
    margin: 2% !important;
  }
  .calendar {
    padding: 0.5rem;
    font-size: 13px;
  }
}

.vuecal__menu,
.vuecal__cell-events-count {
  background-color: #42b983;
}

.closed {
  background:
    #fff7f0
    repeating-linear-gradient(
      -45deg,
      rgba(255, 162, 87, 0.25),
      rgba(255, 162, 87, 0.25) 5px,
      rgba(255, 255, 255, 0) 5px,
      rgba(255, 255, 255, 0) 15px
    ) !important;
  color: #f6984c;
}

</style>
