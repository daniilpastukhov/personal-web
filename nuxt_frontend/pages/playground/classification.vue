<template>
  <div class="classification-page full-page">
    <div class="fl w-75 pl5 pt5 pb3 bg-light-yellow full-page">
      <div class="f2 sans-serif">Classification</div>

      <div class="drop center-label hover-bg-light-blue bg-light-yellow mt5" @dragover.prevent @drop="onDrop">
        <label v-if="!image" class="center-label">
          <span class="code">Select or drop an image here</span><br>
          <input id="image" type="file" accept="image/*" name="image" @change="onChange">
        </label>
        <div v-else>
          <img :src="image" class="img" alt=""/>
        </div>
      </div>
      <div class="pt3 flex">
        <button class="submit-button code hover-bg-light-blue bg-light-yellow" type="submit" :disabled="image == null"
                @click.prevent="submit"> Submit
        </button>
        <button class="remove-button code hover-bg-light-blue bg-light-yellow" @click.prevent="removeImage">Remove
          image
        </button>
      </div>

      <div v-if="label != null && p != null" class="pt3">
        <p>Predicted class: {{ label }}, confidence: {{ p }}</p>
      </div>
    </div>
    <NavbarWidget/>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: 'ClassificationPage',
  components: {},
  data() {
    return {
      image: null,
      max: 1,
      label: null,
      p: null
    }
  },
  methods: {
    handleImage(e) {
      this.image = e.target.files[0]
    },
    submit() {
      const fd = new FormData()
      fd.append('image', this.image)

      axios.post('http://127.0.0.1:5002/predict', fd)
        .then(resp => {
          this.label = resp.data.label
          this.p = resp.data.prob
        })
        .catch(error => console.log(error));
    },
    onDrop(e) {
      e.stopPropagation()
      e.preventDefault()
      const files = e.dataTransfer.files
      this.createFile(files[0])
    },
    onChange(e) {
      const files = e.target.files;
      this.createFile(files[0]);
    },
    createFile(file) {
      if (!file.type.match('image.*')) {
        alert('Select an image');
        return;
      }

      const reader = new FileReader();
      const vm = this;

      reader.onload = function (e) {
        vm.image = e.target.result;
      }
      reader.readAsDataURL(file);
    },
    removeImage() {
      this.image = null
    }
  },
}
</script>

<style>
.drop {
  width: 70%;
  height: 50%;
  border: 3px dashed #000;
  border-radius: 0;
  padding: 5px;
  text-align: center;
  font-size: 20px;
  color: #000;
}

.center-label {
  display: flex;
  justify-content: center;
  align-items: center;
}

input[type="file"] {
  position: absolute;
  opacity: 0;
  z-index: -1;
}

.img {
  border: 1px solid #f6f6f6;
  display: inline-flex;
  height: auto;
  max-height: calc(80%);
  max-width: calc(80%);
  width: auto;
}

.submit-button {
  color: #000;
  border: 2px solid #000;
  border-radius: 0;
  padding: 10px 0;
  margin-right: 2px;
  width: 50%;
  cursor: pointer;
}

.remove-button {
  color: #000;
  border: 2px solid #000;
  border-radius: 0;
  padding: 10px 0;
  margin-left: 2px;
  width: calc(20% - 4px);
  cursor: pointer;
}
</style>
