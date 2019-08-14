<template>
  <v-container>
    <v-layout text-center wrap>
      <v-flex mb-12>
        <h1 class="display-2 font-weight-bold mb-3">Welcome to the Guessing Game</h1>
        <p
          class="subheading font-weight-regular"
        >To start a game please selected a boundary for guessing a number</p>
      </v-flex>

      <v-flex xs12>
        <v-row>
          <v-col cols="12" sm="6" md="4">
            <v-text-field type="number" label="Minimum" required></v-text-field>
          </v-col>
          <v-col cols="12" sm="6" md="4">
            <v-text-field type="number" label="Maximum" required></v-text-field>
          </v-col>
          <v-col cols="12" sm="6" md="4">
            <v-btn @click="startGame">Start the Game</v-btn>
          </v-col>
        </v-row>
      </v-flex>
      
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({})
};
</script>
