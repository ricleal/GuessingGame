<template>
  <v-container class="grey lighten-5">
    <v-layout text-center wrap>
      <v-flex mb-12>
        <h1 class="display-2 font-weight-bold mb-3">Welcome to the Guessing Game</h1>
        <p
          class="subheading font-weight-regular"
        >To start a game please selected a boundary for guessing a number</p>
      </v-flex>
    </v-layout>

    <v-form ref="form" v-model="formStartValid">
      <v-layout row align-center justify-space-between>
        <v-flex md2 xs12 offset-md3>
          <v-text-field
            type="number"
            label="Minimum"
            v-model="minimumValue"
            :rules="minimumRules"
            :error-messages="validMinMax()"
            min="1"
            max="50"
            required
          ></v-text-field>
        </v-flex>
        <v-flex md2 xs12>
          <v-text-field
            type="number"
            label="Maximum"
            v-model="maximumValue"
            :rules="maximumRules"
            :error-messages="validMinMax()"
            min="1"
            max="50"
            id="maximumId"
            required
          ></v-text-field>
        </v-flex>
        <v-flex md2 xs12>
          <v-btn :disabled="!formStartValid" @click="startGame">Start the Game</v-btn>
        </v-flex>
        <v-flex md2 />
      </v-layout>
    </v-form>

    <div v-if="start">
      <v-layout text-center wrap>
        <v-flex mb-12>
          <p>&nbsp;</p>
        </v-flex>
      </v-layout>
      <v-layout text-center wrap>
        <v-flex mb-12>
          <p
            class="subheading font-weight-regular"
          >Choose one of the options below to guess the number</p>
        </v-flex>
      </v-layout>

      <v-form ref="form" v-model="formLessValid">
        <v-layout row align-center justify-space-around>
          <v-flex md3 xs12 offset-md2>
            <v-text-field
              :rules="lessRules"
              type="number"
              label="Less"
              v-model="lessThanValue"
              required
            ></v-text-field>
          </v-flex>
          <v-flex md3 xs12>
            <v-btn :disabled="!formLessValid" @click="isLessThan" color="primary">Less than</v-btn>
          </v-flex>
          <v-flex md1 xs12 />
        </v-layout>
      </v-form>

      <v-form ref="form" v-model="formGreaterValid">
        <v-layout row align-center justify-space-around>
          <v-flex md3 xs12 offset-md2>
            <v-text-field
              :rules="maximumRules"
              type="number"
              label="Greater"
              v-model="greaterThanValue"
              required
            ></v-text-field>
          </v-flex>
          <v-flex md3 xs12>
            <v-btn :disabled="!formGreaterValid" @click="isGreaterThan" color="primary">Greater than</v-btn>
          </v-flex>
          <v-flex md1 xs12 />
        </v-layout>
      </v-form>

      <v-layout row align-center justify-space-around>
        <v-flex md12>
          <p>&nbsp;</p>
        </v-flex>
        <v-flex md1 xs12 offset-md4>
          <v-btn @click="isOdd">Is Odd?</v-btn>
        </v-flex>
        <v-flex md1 xs12>
          <v-btn @click="isEven">Is Even?</v-btn>
        </v-flex>
        <v-flex md3 xs12 />
      </v-layout>

      <v-form ref="form" v-model="formGuessValid">
        <v-layout row align-center justify-space-around>
          <v-flex md12>
            <p>&nbsp;</p>
          </v-flex>
          <v-flex md1 xs12 offset-md4>
            <v-text-field
              :rules="guessRules"
              v-model="guessValue"
              type="number"
              label="Guess?"
              required
            ></v-text-field>
          </v-flex>
          <v-flex md1 xs12>
            <v-btn :disabled="!formGuessValid" @click="guess" color="warning">Guess it?</v-btn>
          </v-flex>
          <v-flex md3 xs12 />
        </v-layout>
      </v-form>
    </div>
    <v-layout text-center wrap>
      <v-flex md12>
        <p>&nbsp;</p>
      </v-flex>
      <v-flex mb-12>
        <h2>{{message}}</h2>
      </v-flex>
    </v-layout>

    <div class="text-center">
      <v-dialog v-model="dialog" width="500">
        <v-card>
          <v-card-title class="headline grey lighten-2" primary-title>Congratulations!!!</v-card-title>
          <v-card-text>
            <br />
            You guessed the number: {{guessValue}}. Now you can play another game!
          </v-card-text>
          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text @click="dialog = false">OK</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </v-container>
</template>

<script>
import Vue from "vue";

/* eslint-disable no-console */

export default {
  data: () => ({
    // start game
    minimumValue: 1,
    maximumValue: 50,
    minimumRules: [v => !!v || "Minimum is required"],
    maximumRules: [v => !!v || "Maximum is required"],
    formStartValid: true,
    start: false, // If false (the game has not started) the game controls are hidden
    // Greater
    greaterThanValue: null,
    greaterRules: [v => !!v || "Greater than value is required"],
    formGreaterValid: true,
    // Less
    lessThanValue: null,
    lessRules: [v => !!v || "Less than value is required"],
    formLessValid: true,
    // Guess
    guessValue: null,
    guessRules: [v => !!v || "Guess value is required"],
    formGuessValid: true,
    dialog: false, // If true shows the dialog when the number is guessed
    // This gives feedback during the game
    message: ""
  }),
  methods: {
    // error message used in the start game to make sure min < max
    validMinMax: function() {
      return this.minimumValue < this.maximumValue
        ? ""
        : "Minimum must be inferior to Maximum";
    },
    startGame: function() {
      Vue.axios.get("/api/start/1/10").then(response => {
        console.log(response.data);
      });
      this.start = true;
      this.message = `Start: Guessing a number from ${this.minimumValue} to ${this.maximumValue}.`;
    },

    isEven: function() {
      Vue.axios
        .get("/api/even")
        .then(response => {
          if (
            response.data["success"] == null ||
            response.data["success"] == false
          ) {
            this.message = "Something wrong!";
          } else {
            console.log(response.data);
            this.message = `Is even? ${response.data["even"]}!`;
          }
        })
        .catch(error => {
          // handle error
          console.log(error);
        });
    },
    isOdd: function() {
      Vue.axios
        .get("/api/odd")
        .then(response => {
          if (
            response.data["success"] == null ||
            response.data["success"] == false
          ) {
            this.message = "Something wrong!";
          } else {
            console.log(response.data);
            this.message = `Is odd? ${response.data["odd"]}!`;
          }
        })
        .catch(error => {
          // handle error
          console.log(error);
        });
    },

    isLessThan: function() {
      Vue.axios
        .get(`/api/less/${this.lessThanValue}`)
        .then(response => {
          if (
            response.data["success"] == null ||
            response.data["success"] == false
          ) {
            this.message = "Something wrong!";
          } else {
            console.log(response.data);
            this.message = `Is less than ${this.lessThanValue}? ${
              response.data["less"]
            }!`;
          }
        })
        .catch(error => {
          // handle error
          console.log(error);
        });
    },
    isGreaterThan: function() {
      Vue.axios
        .get(`/api/greater/${this.greaterThanValue}`)
        .then(response => {
          if (
            response.data["success"] == null ||
            response.data["success"] == false
          ) {
            this.message = "Something wrong!";
          } else {
            console.log(response.data);
            this.message = `Is greater than ${this.greaterThanValue}? ${
              response.data["greater"]
            }!`;
          }
        })
        .catch(error => {
          // handle error
          console.log(error);
        });
    },

    guess: function() {
      Vue.axios
        .get(`/api/guess/${this.guessValue}`)
        .then(response => {
          if (
            response.data["success"] == null ||
            response.data["success"] == false
          ) {
            this.message = "Something wrong!";
          } else {
            console.log(response.data);
            if (response.data["guess"]) {
              this.dialog = true;
              this.start = false;
              this.message = "";
            } else {
              this.message = "You did not guess it :(";
            }
          }
        })
        .catch(error => {
          // handle error
          console.log(error);
        });
    }
  }
};
</script>
