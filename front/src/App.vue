<template>
  <v-app>
    <v-main class="app">
      <router-view />
      <div class="footer">Made by Backend Developer Taewan G</div>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>

<style scoped>
@font-face {
  font-family: "SUIT-Medium";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_suit@1.0/SUIT-Medium.woff2")
    format("woff2");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "SUIT-Regular";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_suit@1.0/SUIT-Regular.woff2")
    format("woff2");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "OTWelcomeRA";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2110@1.0/OTWelcomeRA.woff2")
    format("woff2");
  font-weight: normal;
  font-style: normal;
}

.app {
  font-family: "SUIT-Medium", "SUIT-Regular", "OTWelcomeRA", Cambria;
  background: linear-gradient(#11111d 40%, #333333);
}

.footer {
  margin: 50px 0px 50px 0px;
  text-align: center;
  color: aliceblue;
}
</style>
