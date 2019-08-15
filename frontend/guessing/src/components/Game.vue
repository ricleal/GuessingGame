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
    <v-layout row align-center justify-space-between>
      <v-flex md2 xs12 offset-md3>
        <v-text-field
          type="number"
          label="Minimum"
          v-model="minimumValue"
          :rules="minimumRules"
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
          min="1"
          max="50"
          id="maximumId"
          required
        ></v-text-field>
      </v-flex>
      <v-flex md2 xs12>
        <v-btn @click="startGame">Start the Game</v-btn>
      </v-flex>
      <v-flex md2 />
    </v-layout>

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

      <v-layout row align-center justify-space-around>
        <v-flex md1 xs12 offset-md3>
          <v-text-field type="number" label="Less" v-model="lessThanValue" required></v-text-field>
        </v-flex>
        <v-flex md2 xs12>
          <v-btn @click="isLessThan" color="primary">Less than</v-btn>
        </v-flex>
        <v-flex md1 xs12>
          <v-text-field type="number" label="Greater" v-model="greaterThanValue" required></v-text-field>
        </v-flex>
        <v-flex md2 xs12>
          <v-btn @click="isGreaterThan" color="primary">Greater than</v-btn>
        </v-flex>
        <v-flex md2 />
      </v-layout>

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

      <v-layout row align-center justify-space-around>
        <v-flex md12>
          <p>&nbsp;</p>
        </v-flex>
        <v-flex md1 xs12 offset-md4>
          <v-text-field type="number" label="Guess?" required></v-text-field>
        </v-flex>
        <v-flex md1 xs12>
          <v-btn @click="guess" color="warning">Guess it?</v-btn>
        </v-flex>
        <v-flex md3 xs12 />
      </v-layout>
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
          <v-card-text><br/>You guessed the number. Now you can play another game!</v-card-text>
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
    minimumValue: 1,
    maximumValue: 50,
    greaterThanValue: null,
    lessThanValue: null,
    guessValue: null,
    dialog: false,
    start: false,
    message: "",
    minimumRules: [v => !!v || "Minimum is required"]
  }),
  methods: {
    startGame: function() {
      Vue.axios.get("/api/start/1/10").then(response => {
        console.log(response.data);
      });
      this.start = true;
      this.message = `Start! Guessing a number from ${this.minimumValue} to ${this.maximumValue}.`;
    },
    guess: function() {
      this.dialog = true;
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
      if (this.lessThanValue == null) {
        this.message = "I need a value in field...";
      } else {
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
      }
    },
    isGreaterThan: function() {
      if (this.greaterThanValue == null) {
        this.message = "I need a value in field...";
      } else {
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
      }
    }
  }
};
</script>
