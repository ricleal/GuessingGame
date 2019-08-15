<template>
  <v-container>
    <v-layout text-center wrap>
      <v-flex mb-12>
        <h1 class="display-2 font-weight-bold mb-3">Welcome to the Guessing Game</h1>
        <p
          class="subheading font-weight-regular"
        >To start a game please selected a boundary for guessing a number</p>
      </v-flex>
    </v-layout>
    <v-layout row justify-space-between>
      <v-flex md3>
        <v-text-field type="number" label="Minimum" value="1" min="1" max="50" required></v-text-field>
      </v-flex>
      <v-flex md3>
        <v-text-field type="number" label="Maximum" value="50" min="1" max="50" required></v-text-field>
      </v-flex>
      <v-flex md3>
        <v-btn @click="startGame">Start the Game</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Vue from 'vue';

export default {
  data: () => ({}),
  methods: {
    startGame: () => {
      Vue.axios.get("/api/start/1/10").then(response => {
        /* eslint-disable no-console */
        console.log(response.data);
      });
    }
  }
};
</script>
