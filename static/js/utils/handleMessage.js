export function handleMessage(messageId, type, message) {
  const messageElement = document.getElementById(messageId);
  if (!messageElement) return;

  messageElement.querySelector('.message__text').textContent = message;;

  messageElement.classList.remove('message--success', 'message--error');

  if (type === 'success') {
    messageElement.classList.add('message--success');
  } else {
    messageElement.classList.add('message--error');
  }

  messageElement.classList.add('message--show');

  setTimeout(() => {
    messageElement.classList.remove('message--show');
  }, 4000);
}
