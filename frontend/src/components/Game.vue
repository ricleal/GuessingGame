<template>
  <v-container class="grey lighten-5">
    <v-row>
      <v-col cols="12">
        
        <v-row align="start" justify="center" class="grey lighten-5">
          <h1 class="display-2 font-weight-bold mb-3">Welcome to the Guessing Game</h1>
          <p class="subheading font-weight-regular">
            To start a game please selected a boundary for guessing a number and the number of tries
            until you can guess the number.
          </p>
        </v-row>

        <v-form ref="formStart" @submit.prevent v-model="formStartValid">
          <v-row align="start" justify="center" class="grey lighten-5">
            <v-col cols="4" md="2">
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
            </v-col>
            <v-col cols="4" md="2">
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
            </v-col>
            <v-col cols="4" md="2">
              <v-text-field
                type="number"
                label="Tries"
                v-model="triesValue"
                :rules="triesRules"
                min="1"
                max="50"
                id="triesId"
                required
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row align="start" justify="center" class="grey lighten-5">
            <v-col cols="12" md="2">
              <v-btn type="submit" :disabled="!formStartValid" @click="startGame">Start a new game</v-btn>
            </v-col>
          </v-row>
        </v-form>

        <!-- Game starts here -->
        <div v-if="start">
          <v-row align="start" justify="center" class="grey lighten-5">
            <p class="font-weight-regular">Choose one of the options below to guess the number</p>
          </v-row>

          <v-form @submit.prevent ref="formLess" v-model="formLessValid">
            <v-row align="start" justify="center" class="grey lighten-5">
              <v-col cols="6" md="2">
                <v-text-field
                  :rules="lessRules"
                  type="number"
                  label="Less"
                  v-model="lessThanValue"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="6" md="2">
                <v-btn
                  type="submit"
                  :disabled="!formLessValid"
                  @click="isLessThan"
                  color="primary"
                >Less than</v-btn>
              </v-col>
            </v-row>
          </v-form>

          <v-form @submit.prevent ref="formGreater" v-model="formGreaterValid">
            <v-row align="start" justify="center" class="grey lighten-5">
              <v-col cols="6" md="2">
                <v-text-field
                  :rules="maximumRules"
                  type="number"
                  label="Greater"
                  v-model="greaterThanValue"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="6" md="2">
                <v-btn
                  type="submit"
                  :disabled="!formGreaterValid"
                  @click="isGreaterThan"
                  color="primary"
                >Greater than</v-btn>
              </v-col>
            </v-row>
          </v-form>

          <v-row align="start" justify="center" class="grey lighten-5">
            <v-col cols="6" md="2">
              <v-btn @click="isOdd">Is it odd?</v-btn>
            </v-col>
            <v-col cols="6" md="2">
              <v-btn @click="isEven">Is it even?</v-btn>
            </v-col>
          </v-row>

          <!-- Guess number -->
          <div v-if="counterComputed == 0">
            <v-form ref="formGuess" @submit.prevent v-model="formGuessValid">
              <v-row align="start" justify="center" class="grey lighten-5">
                <p class="font-weight-regular">Guess a number?</p>
              </v-row>

              <v-row align="start" justify="center" class="grey lighten-5">
                <v-col cols="6" md="2">
                  <v-text-field
                    :rules="guessRules"
                    v-model="guessValue"
                    type="number"
                    label="Guess?"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="6" md="2">
                  <v-btn
                    type="submit"
                    :disabled="!formGuessValid"
                    @click="guess"
                    color="warning"
                  >Guess it?</v-btn>
                </v-col>
              </v-row>
            </v-form>
          </div>
          <!--  END: counterComputed -->
        </div>
        <!-- END: visible -->
      </v-col>
    </v-row>

    <!-- footer -->
    <v-row align="start" justify="center" class="grey lighten-5">
      <v-col cols="12" md="6">
        <v-card max-width="400" class="mx-auto">
          <v-card-title>{{message}}</v-card-title>
          <div class="text-center">
            <v-badge>
              <template v-slot:badge>{{counterComputed}}</template>
              <v-icon v-if="counterComputed == 0">lock_open</v-icon>
              <v-icon v-else>lock</v-icon>
            </v-badge>
          </div>
        </v-card>
      </v-col>
    </v-row>

    <!-- Won / Lost dialog -->
    <div class="text-center">
      <v-dialog v-model="dialog" width="500">
        <v-card>
          <v-card-title class="headline grey lighten-2" primary-title>You tried to guess it and...</v-card-title>
          <v-card-text>
            <br />
            <h2>{{this.winMessage }}</h2>
            <br />
            <p>You can play another game...</p>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text @keyup.enter="dialog = false" @click="dialog = false">OK</v-btn>
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
    maximumValue: 20,
    triesValue: 5,
    minimumRules: [v => !!v || "Minimum is required"],
    maximumRules: [v => !!v || "Maximum is required"],
    triesRules: [v => !!v || "Tries is required"],
    formStartValid: true, // all forms start valid
    start: false, // If false (the game has not started) the game controls are hidden
    counter: 0, // counts the number of tries before one can guess the number
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
    winMessage: "", //Message displayed when one guesses the number
    // This gives feedback during the game
    message: ""
  }),
  computed: {
    // because in depends on the input form and on the counter it as to be calculated in real time
    counterComputed: function() {
      let value = this.triesValue - this.counter;
      if (value >= 0) {
        return value;
      } else {
        return 0;
      }
    }
  },
  methods: {
    // error message used in the start to make sure min < max
    validMinMax: function() {
      return this.minimumValue < this.maximumValue
        ? ""
        : "Minimum must be inferior to Maximum";
    },
    startGame: function() {
      Vue.axios
        .get(`/api/start/${this.minimumValue}/${this.maximumValue}`)
        .then(response => {
          if (
            response.data["success"] == null ||
            response.data["success"] == false
          ) {
            this.message = "Something wrong!";
          } else {
            this.start = true;
            this.message = `Guessing a number from ${this.minimumValue} to ${this.maximumValue}.`;
            this.winMessage = "";
            this.counter = 0;
          }
        })
        .catch(error => {
          // handle error
          console.log(error);
        });
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
            this.message = `Is it even? ${response.data["even"]}!`;
            this.counter++;
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
            this.message = `Is it odd? ${response.data["odd"]}!`;
            this.counter++;
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
            this.message = `Is it less than ${this.lessThanValue}? ${
              response.data["less"]
            }!`;
            this.counter++;
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
            this.message = `Is it greater than ${this.greaterThanValue}? ${
              response.data["greater"]
            }!`;
            this.counter++;
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
            this.dialog = true;
            this.start = false;
            this.message = "";
            this.winMessage = response.data["message"];
            this.counter = 0;
            this.guessValue = null;
            this.lessThanValue = null;
            this.greaterThanValue = null;
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
