export function completeHandler(data) {
  localStorage.setItem("statusData", JSON.stringify(data));
  location.reload();
}
