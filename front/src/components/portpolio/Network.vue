<template>
  <v-row class="row-content-center">
    <v-col cols="12">
      <img
        src="../../assets/github.png"
        alt=""
        class="network-icon"
        @click="goToGitHub"
      />
      <img
        src="../../assets/codeforces.png"
        alt=""
        class="network-icon"
        @click="goToCodeForces"
      />
      <img
        src="../../assets/boj.png"
        alt=""
        class="network-icon"
        @click="goToBOJ"
      />
      <img
        src="../../assets/linkedin.png"
        alt=""
        class="network-icon"
        @click="goToLinkedIn"
      />
      <img
        src="../../assets/instagram.png"
        alt=""
        class="network-icon"
        @click="goToInstagram"
      />
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "Network",
  methods: {
    goToGitHub() {
      open("https://github.com/Taewan-Gu");
    },
    goToCodeForces() {
      open("https://codeforces.com/profile/muvissum");
    },
    goToBOJ() {
      open("https://solved.ac/profile/fksk94");
    },
    goToLinkedIn() {
      open("https://www.linkedin.com/in/taewan-gu-a367b3228");
    },
    goToInstagram() {
      open("https://www.instagram.com/twn.gg");
    },
  },
};
</script>

<style scoped>
.network-icon:hover {
  border-radius: 100px;
  box-shadow: 0px 0px 10px 5px #555555;
  cursor: pointer;
}

.network-icon {
  width: 30px;
  height: 30px;
  margin-left: 15px;
  margin-right: 15px;
  transition: 0.2s;
  border-radius: 100px;
  cursor: pointer;
}
</style>
