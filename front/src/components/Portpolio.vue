<template>
  <div class="portpolio">
    <Profile />
    <Resume />
    <AboutMe />
    <Network />
    <Experience />
    <Projects />
  </div>
</template>

<script>
import Profile from "@/components/portpolio/Profile.vue";
import Resume from "@/components/portpolio/Resume.vue";
import AboutMe from "@/components/portpolio/AboutMe.vue";
import Network from "@/components/portpolio/Network.vue";
import Experience from "@/components/portpolio/Experience.vue";
import Projects from "@/components/portpolio/Projects.vue";

export default {
  name: "Portpolio",
  components: {
    Profile,
    Resume,
    AboutMe,
    Network,
    Experience,
    Projects,
  },
  data: () => ({}),
};
</script>

<style scoped>
.portpolio {
  margin-left: auto;
  margin-right: auto;
  margin-top: 30px;
  padding: 100px 50px 50px 50px;
  width: 900px;
  border: #222222 1px solid;
  border-radius: 20px;
  box-shadow: 0px 0px 10px 5px #555555;
}

@media screen and (max-width: 980px) {
  .portpolio {
    margin-left: 40px;
    margin-right: 40px;
    margin-top: 30px;
    padding: 40px 30px 20px 30px;
    width: auto;
    border: #222222 1px solid;
    border-radius: 20px;
    box-shadow: 0px 0px 10px 5px #555555;
  }
}

.row-content-center {
  margin-top: 30px;
  margin-bottom: 50px;
  justify-content: center;
  text-align: center;
  color: aliceblue;
}
</style>
