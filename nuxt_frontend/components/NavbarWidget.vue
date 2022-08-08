<template>
  <div ref="navbar" class="fl navbar pv5 w-25 min-w-25 min-h-100 hover-bg-light-blue bg-light-yellow full-page">
    <ul class="list mt0">
      <li v-for="el in menu_items"
          :key="el.name"
          class="lh-copy mt0 pb3 pr5">
        <a v-if="el.type === 'extended' || el.type === 'back'"
           class="f2 no-underline link-color sans-serif descripcion"
           @click="el = menuClick(el)">
          <ArrowLeft v-if="el.type === 'back'" size="36" />
          <span v-else>{{ el.name + " ....." }}</span>
        </a>
        <a v-else :href="el.url" class="f2 no-underline link-color sans-serif descripcion">
          {{ el.name }}
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import ArrowLeft from 'vue-material-design-icons/ArrowLeft.vue';

export default {
  name: 'NavbarWidget',
  components: {
    ArrowLeft,
  },
  data: () => ({
    menu_items: [
      {
        name: 'Home',
        type: 'link',
        url: '/',
      },
      {
        name: 'Playground',
        type: 'extended',
        url: '/playground',
        sub_items: [
          {
            name: 'Back',
            type: 'back',
            url: '#',
          },
          {
            name: 'Segmentation',
            type: 'link',
            url: '/playground/segmentation',
          },
          {
            name: 'Classification',
            type: 'link',
            url: '/playground/classification',
          },
        ],
      },
      {
        name: 'About me',
        type: 'link',
        url: '/about',
      },
      {
        name: 'Curriculum vitae',
        type: 'link',
        url: '/cv',
      },
    ],
  }),
  methods: {
    menuClick(el) {
      if (el.type === 'back') {
        return this.menuGoBack(el)
      }
      this.prev_items = this.menu_items
      this.menu_items = el.sub_items
      return this.menu_items
    },
    menuGoBack(el) {
      this.menu_items = this.prev_items
      return this.menu_items
    },
  }
}
</script>

<style>
.link-color {
  color: #000;
}

.min-w-25 {
  min-width: calc(max(25%, 400px));
}

.navbar {
  border-left: 3px dashed #000;
}
</style>
