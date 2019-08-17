<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Guessing</span>
        <span class="font-weight-light">Game</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-content>
      <Game />
    </v-content>
  </v-app>
</template>

<script>
import Game from "./components/Game";

export default {
  name: "App",
  components: {
    Game
  },
  data: () => ({
    //
  })
};
</script>
