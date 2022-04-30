import axios from "axios";

const BASE_URL = "https://www.getgoalswith.site/api/";

const URL_MAP = {
    "resume": BASE_URL + "resume"
}

export function downloadResume() {
    axios.get(URL_MAP.resume)
    .then(() => {})
    .catch(() => alert("ERROR"))
}