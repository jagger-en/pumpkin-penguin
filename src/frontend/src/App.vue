<script setup>
import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'

</script>

<script>
export default {
  data: () => ({
    draggables: [
      {
        // The id (or however you name it), will help you find which event to delete
        // from the callback triggered on drop into Vue Cal.
        id: 1,
        title: 'Ext. Event 1',
        content: 'content 1',
        duration: 60
      },
      {
        id: 2,
        title: 'Ext. Event 2',
        content: 'content 2',
        duration: 30
      },
      {
        id: 3,
        title: 'Ext. Event 3',
        content: 'content 3'
        // No defined duration here: will default to 2 hours.
      }
    ]
  }),
  methods: {
    onEventDragStart (e, draggable) {
      // Passing the event's data to Vue Cal through the DataTransfer object.
      e.dataTransfer.setData('event', JSON.stringify(draggable))
      e.dataTransfer.setData('cursor-grab-at', e.offsetY)
    },
    // The 3 parameters are destructured from the passed $event in @event-drop="onEventDrop".
    // `event` is the final event as Vue Cal understands it.
    // `originalEvent` is the event that was dragged into Vue Cal, it can come from the same
    //  Vue Cal instance, another one, or an external source.
    // `external` is a boolean that lets you know if the event is not coming from any Vue Cal.
    onEventDrop ({ event, originalEvent, external }) {
      // If the event is external, delete it from the data source on drop into Vue Cal.
      // If the event comes from another Vue Cal instance, it will be deleted automatically in there.
      if (external) {
        const extEventToDeletePos = this.draggables.findIndex(item => item.id === originalEvent.id)
        if (extEventToDeletePos > -1) this.draggables.splice(extEventToDeletePos, 1)
      }
    }
  }
}

data: () => ({
  minCellWidth: 400,
  minSplitWidth: 0,
  splitDays: [
    // The id property is added automatically if none (starting from 1), but you can set a custom one.
    // If you need to toggle the splits, you must set the id explicitly.
    { id: 1, class: 'tb1', label: 'TB1', hide: false },
    { id: 2, class: 'tb2', label: 'TB2', hide: false },
    { id: 3, class: 'vb1', label: 'VB1', hide: false },
    { id: 4, class: 'vb2', label: 'VB2', hide: false },
    { id: 5, class: 'u'  , label: 'U'  , hide: false }
  ],
  events: [
    {
      start: '2018-11-19 10:35',
      end: '2018-11-19 11:30',
      title: 'Doctor appointment',
      content: '<i class="icon material-icons">local_hospital</i>',
      class: 'health',
      split: 1 // Has to match the id of the split you have set (or integers if none).
    },
    {
      start: '2018-11-19 18:30',
      end: '2018-11-19 19:15',
      title: 'Dentist appointment',
      content: '<i class="icon material-icons">local_hospital</i>',
      class: 'health',
      split: 2
    },
    {
      start: '2018-11-20 18:30',
      end: '2018-11-20 20:30',
      title: 'Crossfit',
      content: '<i class="icon material-icons">fitness_center</i>',
      class: 'sport',
      split: 1
    }
  ]
})

</script>

<template>
  <!-- Bootstrap -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

  <main class="container">
    <div class="row align-items-start">
      <div class="patient-rack col">

        <!-- WIP: add patient -->
        <!-- Button trigger modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
          Add patient
        </button>
        <!-- Modal -->
        <div class="modal-dialog modal-dialog-centered fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="staticBackdropLabel">Modal title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                ...
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Understood</button>
              </div>
            </div>
          </div>
        </div>

        <!-- WIP: patient card list -->
        <!-- Three HTML5 draggable events. -->
        <div class="external-event card"
             style="margin: 1%;"
             v-for="(item, i) in draggables"
             :key="i"
             draggable="true"
             @dragstart="onEventDragStart($event, item)">
             <strong>{{ item.title }}</strong>
             ({{ item.duration ? `${item.duration} min` : 'no duration' }})
          <div>{{ item.content }}</div>
        </div>

      </div>
      <div class="calendar col-8">

        <!-- The main schedule view -->
        <button @click="minCellWidth = minCellWidth ? 0 : 400">
          {{ minCellWidth ? 'min cell width: 400px' : 'Add min cell width' }}
        </button>
        <button @click="minSplitWidth = minSplitWidth ? 0 : 200">
          {{ minSplitWidth ? 'min split width: 200px' : 'Add min split width' }}
        </button>
        <!-- For loop for splitDays[i] -->
        <button class="button" @click="splitDays[0].hide = !splitDays[0].hide">
          Show/Hide TB1
        </button>
        <button class="button" @click="splitDays[1].hide = !splitDays[1].hide">
          Show/Hide TB2
        </button>
        <button class="button" @click="splitDays[2].hide = !splitDays[2].hide">
          Show/Hide VB1
        </button>
        <button class="button" @click="splitDays[3].hide = !splitDays[3].hide">
          Show/Hide VB2
        </button>
        <button class="button" @click="splitDays[4].hide = !splitDays[4].hide">
          Show/Hide U
        </button>

        <vue-cal
          style="padding: 2.5vh; height: 98vh;"
          hide-view-selector
          hide-weekends
          :disable-views="['years', 'year', 'month', 'day']"
          :time-from="8 * 60"
          :time-to="18 * 60"
          :time-step="30"
          :snap-to-time="15"
          editable-events
          @event-drop="onEventDrop"
          :events="events"
          :split-days="splitDays"
          :min-cell-width="minCellWidth"
          :min-split-width="minSplitWidth">
        </vue-cal>
      </div>

    </div>
  </main>

  <!-- Bootstrap JS -->
  <!-- <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script> -->

</template>

<style scoped>
  .html {
    overflow: hidden;
    width: 100vh;
    height: 100vh;
    margin: 0% !important;
  }
  .container {
    max-width: 100% !important;
    margin-right: 2% !important;
    margin-left: 2% !important;
  }

  /* You can easily set a different style for each split of your days. */
  .vuecal__cell-split.tb1 {background-color: rgba(221, 238, 255, 0.5);}
  .vuecal__cell-split.tb2 {background-color: rgba(255, 232, 251, 0.5);}
  .vuecal__cell-split.vb1 {background-color: rgba(221, 255, 239, 0.5);}
  .vuecal__cell-split.vb2 {background-color: rgba(255, 250, 196, 0.5);}
  .vuecal__cell-split.u   {background-color: rgba(255, 206, 178, 0.5);}

  /* Different color for different event types. */
  /* .vuecal__event.leisure {background-color: rgba(253, 156, 66, 0.9);border: 1px solid rgb(233, 136, 46);color: #fff;} */
  /* .vuecal__event.health {background-color: rgba(164, 230, 210, 0.9);border: 1px solid rgb(144, 210, 190);} */
  /* .vuecal__event.sport {background-color: rgba(255, 102, 102, 0.9);border: 1px solid rgb(235, 82, 82);color: #fff;} */
</style>
