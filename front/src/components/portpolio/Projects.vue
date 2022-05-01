<template>
  <v-row class="row-content-center">
    <v-col cols="12" class="subtitle">Projects</v-col>
    <Card
      v-for="(project, idx) in projects"
      :key="idx"
      :projectTitle="project.projectTitle"
      :projectPeriod="project.projectPeriod"
      :projectContents="project.projectContents"
      :redirectUrl="project.redirectUrl"
    />
    <v-col cols="12"> </v-col>
  </v-row>
</template>

<script>
import Card from "@/components/portpolio/project/Card.vue";

export default {
  name: "Projects",
  components: {
    Card,
  },
  data() {
    return {
      projects: [
        {
          projectTitle: "인잇(InIT)",
          projectPeriod: "2021.12 ~ ing",
          projectContents: [
            "부트캠프 졸업자 커뮤니티[APP]",
            "백엔드 담당",
            "SpringBoot, JPA, Postgresql",
          ],
          redirectUrl: "https://apps.apple.com/kr/app/%EC%9D%B8%EC%9E%87-init/id1620744100",
        },
        {
          projectTitle: "어개인(Agaein)",
          projectPeriod: "2021.08 ~ ing",
          projectContents: [
            "크롤링 기반 실종동물 찾기 사이트[WEB]",
            "백엔드 담당",
            "ExpressJS, FastAPI, GraphQL, Postgresql",
          ],
          redirectUrl: "https://www.agaein.com",
        },
        {
          projectTitle: "코드런(CODE:RUN)",
          projectPeriod: "2021.04 ~ 2021.05",
          projectContents: [
            "동영상 지식 공유 플랫폼[WEB]",
            "백엔드 담당",
            "FastAPI, k8s, HLS, Mysql",
          ],
          redirectUrl: "https://github.com/Taewan-Gu/CODE-RUN",
        },
        {
          projectTitle: "플라넷(FlaNET)",
          projectPeriod: "2021.02 ~ 2021.04",
          projectContents: [
            "시계열 데이터 기반 AI/ML 블록코딩[WEB]",
            "백엔드 담당",
            "FastAPI, Tensorflow, Mysql",
          ],
          redirectUrl: "https://github.com/Taewan-Gu/FlaNET",
        },
        {
          projectTitle: "누보(NUVO)",
          projectPeriod: "2021.01 ~ 2021.02",
          projectContents: [
            "VR 여행 사진 전시 플랫폼[WEB, APP]",
            "프론트엔드 담당",
            "Vuejs, Adobe XD, React Native",
          ],
          redirectUrl: "https://github.com/Taewan-Gu/NUVO",
        },
        {
          projectTitle: "학술대회 논문",
          projectPeriod: "2019.07 ~ 2019.10",
          projectContents: [
            "한글 형태소 분석을 통한 식당 키워드 추출",
            "제 3 저자",
            "Branching Entropy, TF-IDF, SoyNLP",
          ],
          redirectUrl:
            "https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE09262396",
        },
      ],
    };
  },
};
</script>

<style scoped>
.subtitle {
  font-size: 28px;
}
</style>
