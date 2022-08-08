<template>
  <div class="about-page full-page">
    <div class="fl w-75 pa5 bg-light-yellow full-page">
      <div class="f-subheadline sans-serif">About me</div>
    </div>
    <NavbarWidget/>
  </div>
</template>

<script>
export default {
  name: 'AboutPage',
}
</script>

<style>
.full-page {
  height: 100vh;
}

.light-yellow {
  color: #FFFCEB;
}

.bg-light-yellow {
  background-color: #FFFCEB;
}

.light-blue {
  color: #EBF5FF;
}

.bg-light-blue {
  background-color: #EBF5FF;
}

.hover-bg-light-blue:hover {
  background-color: #EBF5FF;
}
</style>
