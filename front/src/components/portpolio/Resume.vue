<template>
  <v-row class="row-content-center resume-box">
    <v-col cols="5" class="resume" @click="downloadResume">Resume.pdf</v-col>
    <v-col cols="2"></v-col>
    <v-col cols="5" class="resume" @click="showResume">Resume.html</v-col>
  </v-row>
</template>

<script>
export default {
  name: "Resume",
  methods: {
    downloadResume() {
      open("https://taewan.page/api/resume/download?" + Date.now());
    },
    showResume() {
      open("https://taewan.page/api/resume/html?" + Date.now());
    },
  },
};
</script>

<style scoped>
.resume-box {
  padding: 0px 30px 0px 30px;
}

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
