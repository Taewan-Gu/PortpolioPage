<template>
  <v-row class="row-content-center">
    <v-col cols="3"></v-col>
    <v-col cols="6" class="resume">Resume</v-col>
    <v-col cols="3"></v-col>
  </v-row>
</template>

<script>
export default {
  name: "Resume",
};
</script>

<style scoped>
.resume:hover {
  border: #222222 1px solid;
  border-radius: 10px;
  box-shadow: 2px 2px 5px 2px #555555;
  cursor: pointer;
}

.resume {
  transition: 0.2s;
  border: #222222 1px solid;
  border-radius: 10px;
  box-shadow: -2px -2px 5px 2px #555555;
  cursor: pointer;
}
</style>
