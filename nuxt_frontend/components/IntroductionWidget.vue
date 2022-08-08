<template>
  <div class="fl w-75 pa5 bg-light-yellow full-page">
    <typewriter :type-interval="20">
      <div class="f-subheadline sans-serif">Hello,</div>
      <span class="f2 mt0 black sans-serif lh-copy">
      I am Daniil and I am machine learning enthusiast!<br>
      Welcome to my personal website!<br>
      You can find my CV <a href="#"> here</a>.<br>
      Playground is a place where I experiment with machine learning algorithms. Everybody is welcomed to try it out!<br>
    </span>
    </typewriter>
  </div>
</template>

<script>
import Typewriter from "typewriter-vue";

export default {
  name: 'IntroductionWidget',
  components: {
    Typewriter,
  },
  data: () => ({}),
}
</script>

<style>
</style>
