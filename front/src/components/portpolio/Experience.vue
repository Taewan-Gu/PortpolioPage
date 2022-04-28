<template>
  <v-row class="row-content-center">
    <v-col cols="12" class="subtitle">Experience</v-col>
    <Card
      v-for="(experience, idx) in experiences"
      :key="idx"
      :experienceTitle="experience.experienceTitle"
      :experiencePeriod="experience.experiencePeriod"
      :experienceContents="experience.experienceContents"
      :redirectUrl="experience.redirectUrl"
    />
  </v-row>
</template>

<script>
import Card from "@/components/portpolio/experience/Card.vue";

export default {
  name: "Experience",
  data() {
    return {
      experiences: [
        {
          experienceTitle: "현대카드",
          experiencePeriod: "2021.12 ~ 2022.05",
          experienceContents: [
            "실시간 데이터 플랫폼 개발[Associate]",
            "Universe Echo 개발",
          ],
          redirectUrl: "https://www.hyundaicard.com",
        },
        {
          experienceTitle: "엔테크서비스",
          experiencePeriod: "2021.07 ~ 2021.09",
          experienceContents: [
            "네이버 예약시스템 클론코딩[인턴]",
            "인프라 시스템 개발[사원]",
          ],
          redirectUrl: "https://www.nts-corp.com",
        },
        {
          experienceTitle: "삼성 청년 SW 아카데미",
          experiencePeriod: "2020.07 ~ 2021.05",
          experienceContents: [
            "4기 우수 20인 선정",
            "알고리즘 경진대회(싸피 레이스) 3등",
            "삼성전자 네트워크 사업부 연계 프로젝트 진행",
          ],
          redirectUrl: "https://www.ssafy.com",
        },
      ],
    };
  },
  components: {
    Card,
  },
};
</script>

<style scoped>
.subtitle {
  font-size: 28px;
}
</style>
