<template>
  <div class="game">
    <h1>{{ msg }}</h1>

    <button v-on:click="start">Start Game</button>
    <input v-model.number="min" type="number" placeholder="Minimum">
    <input v-model.number="max" type="number" placeholder="Maximum">
    
    <p>
    <button v-on:click="start">Even</button>
    <button v-on:click="start">Odd</button>
    </p>
    
    <p>
      <button v-on:click="start">Greater then</button>
      <input v-model.number="greaterThan" type="number" placeholder="Greater than">
    </p>

    <p>
      <button v-on:click="start">Less then</button>
      <input v-model.number="lessThan" type="number" placeholder="Less than">
    </p>

    <p>
      <button v-on:click="start">Guess?</button>
      <input v-model.number="guess" type="number" placeholder="Guess">
    </p>
    
  </div>
</template>

<script>
export default {
  name: 'Game',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
