<template>
  <v-row class="row-content-center">
    <img src="../../assets/1.jpg" class="profile-image" alt="" />
    <v-col cols="12" class="intro">안녕하세요 백엔드개발자 구태완입니다</v-col>
  </v-row>
</template>

<script>
export default {
  name: "Profile",
};
</script>

<style scoped>
.profile-image {
  width: 250px;
  height: 250px;
  border-radius: 250px;
}

@media screen and (max-width: 800px) {
  .profile-image {
    width: 220px;
    height: 220px;
    border-radius: 220px;
  }
}

@media screen and (max-width: 600px) {
  .profile-image {
    width: 200px;
    height: 200px;
    border-radius: 200px;
  }
}

@media screen and (max-width: 500px) {
  .profile-image {
    width: 180px;
    height: 180px;
    border-radius: 180px;
  }
}

.intro {
  margin-top: 30px;
  font-size: 18px;
}
</style>
