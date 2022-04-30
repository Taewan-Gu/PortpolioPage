import axios from "axios";

const BASE_URL = "https://taewan.page/api/";

const URL_MAP = {
    "resumeDownload": BASE_URL + "resume/download"
}

export function downloadResume() {
    axios.get(URL_MAP.resumeDownload)
    .then(() => {})
    .catch(() => alert("ERROR"))
}