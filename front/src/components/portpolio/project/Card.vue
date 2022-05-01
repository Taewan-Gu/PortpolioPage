<template>
  <v-col v-if="windowWidth > 950" cols="5" class="card" @click="openPage()">
    <div class="project-title">{{ projectTitle }}</div>
    <div class="project-period">{{ projectPeriod }}</div>
    <div
      v-for="(content, idx) in projectContents"
      :key="idx"
      class="project-content"
    >
      {{ content }}
    </div>
  </v-col>
  <v-col v-else cols="11" class="card" @click="openPage()">
    <div class="project-title">{{ projectTitle }}</div>
    <div class="project-period">{{ projectPeriod }}</div>
    <div
      v-for="(content, idx) in projectContents"
      :key="idx"
      class="project-content"
    >
      {{ content }}
    </div>
  </v-col>
</template>

<script>
export default {
  name: "Card",
  data() {
    return {
      windowWidth: window.innerWidth,
    };
  },
  props: {
    projectTitle: [String, Object],
    projectPeriod: [String, Object],
    projectContents: [Array, Object],
    redirectUrl: [String, Object],
  },
  methods: {
    openPage() {
      open(this.redirectUrl);
    },
  },
};
</script>

<style scoped>
.card:hover {
  margin-left: auto;
  margin-right: auto;
  margin-top: 30px;
  padding: 30px 30px 30px 30px;
  border: antiquewhite 1px solid;
  border-radius: 20px;
  background-color: #343434;
  color: antiquewhite;
  box-shadow: 3px -3px 10px 5px #060606;
}

.card {
  margin-left: auto;
  margin-right: auto;
  margin-top: 30px;
  padding: 30px 30px 30px 30px;
  border: #222222 1px solid;
  border-radius: 20px;
  box-shadow: -3px 3px 10px 5px #060606;
  cursor: pointer;
  transition: 0.2s;
}

.project-title {
  font-weight: 550;
  font-size: 20px;
}

.project-period {
  font-size: 12px;
  margin-bottom: 20px;
  margin-top: 5px;
}

.project-content {
  font-size: 14px;
}
</style>
