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

.intro {
  margin-top: 30px;
  font-size: 18px;
}
</style>
