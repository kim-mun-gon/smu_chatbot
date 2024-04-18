function displayMessage(text, sender) {
  const chatBox = document.getElementById('chat-box');
  const messageDiv = document.createElement('div');
  messageDiv.textContent = text;
  messageDiv.classList.add('message', sender + '-message');

  // 메시지 길이에 따라 상자 크기 조절
  const tempDiv = document.createElement('div');
  tempDiv.style.display = 'inline-block';
  tempDiv.style.visibility = 'hidden'; 
  tempDiv.textContent = text;
  document.body.appendChild(tempDiv);
  
  // 일정 길이 이상일 경우 상자 크기 조절
  const maxWidth = chatBox.clientWidth * 0.7; 
  if (tempDiv.clientWidth < maxWidth) {
    messageDiv.style.width = `${tempDiv.clientWidth + 20}px`; 
  } else {
    messageDiv.style.width = `${maxWidth}px`;
  }
  
  // tempDiv 제거
  document.body.removeChild(tempDiv);

  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight; // 새 메시지로 스크롤
}

document.getElementById('user-input').addEventListener('keypress', function(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      const messageText = this.value.trim();
      if (messageText) {
          displayMessage(messageText, 'user');
          this.value = ''; // 입력창 초기화
          
          fetch('/ask', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/x-www-form-urlencoded',
              },
              body: `question=${encodeURIComponent(messageText)}`,
          })
          .then(response => response.json())
          .then(data => {
              displayMessage(data.answer, 'bot');
          });
      }
  }
});

