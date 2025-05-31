function generateQuiz(containerId, title, question, options, correctAnswers) {
    const container = document.getElementById(containerId);
    container.innerHTML = ''; // Clear previous content

    const questionTitle = document.createElement('p');
    questionTitle.textContent = title;
    questionTitle.style.fontWeight = 'bold';
    questionTitle.style.color = '#0E76BC';
    questionTitle.style.marginBottom = '0px';
    container.appendChild(questionTitle);

    const questionElement = document.createElement('p');
    questionElement.innerHTML = question;
    questionElement.style.marginBottom = '5px';
    container.appendChild(questionElement);

    const form = document.createElement('form');
    form.id = `form-${containerId}`; // Unique form ID to avoid conflicts

    const messageElement = document.createElement('div');
    messageElement.style.opacity = 0;
    messageElement.style.transition = 'opacity 0.2s ease-in-out';
    messageElement.style.display = 'none';
    messageElement.style.color = 'black';
    messageElement.style.padding = '10px';
    messageElement.style.borderRadius = '5px';
    messageElement.style.marginTop = '10px';
    messageElement.style.fontSize = '15px';

    const messageBody = document.createElement('div');
    messageElement.appendChild(messageBody);

    Object.entries(options).forEach(([option, explanation], index) => {
        const div = document.createElement('div');
        div.className = 'form-check';
        div.style.display = 'grid';
        div.style.gridTemplateColumns = 'auto 1fr'; // Ensures radio button and text alignment
        div.style.alignItems = 'center'; // Align radio button with text vertically
        div.style.marginBottom = '5px';

        const input = document.createElement('input');
        input.type = 'radio';
        input.name = `quiz-${containerId}`; // Unique name for each quiz instance
        input.value = option;
        input.className = 'form-check-input me-2'; // Added margin for spacing
        input.id = `option-${containerId}-${index}`;
        input.style.borderColor = '#4853A4'; // Radio button outline
        input.style.boxShadow = 'none';  // Remove brief occurances of transparent fill when clicked
        input.style.outline = 'none';  // Remove brief occurances of transparent fill when clicked

        input.addEventListener('change', function () {
            messageElement.style.display = 'none';
            messageElement.style.opacity = 0;

            isCorrect = false
            if (Array.isArray(correctAnswers)) {
                isCorrect = correctAnswers.some(ans => ans === option);
            } else {
                isCorrect = correctAnswers === option
            }

            if (isCorrect) {
                const emojis = ["🍀", "🎉", "🌈", "🚀", "🌟", "✨", "💯"];
                const emoji = emojis[~~(Math.random() * emojis.length)];
                messageBody.innerHTML = `<strong style="color: #0E76BC !important; font-size: 16px">Correct! &nbsp;${emoji}</strong><br>${explanation}`;
                messageElement.style.backgroundColor = '#DBF1FF'; // Light background for content
                messageElement.style.borderLeft = '5px solid #0E76BC'; // Left border styling
            } else {
                messageBody.innerHTML = `<strong style="color: #003366 !important; font-size: 16px;">Incorrect</strong><br>${explanation}`;
                messageElement.style.backgroundColor = '#F0F7FF'; // Light background for content
                messageElement.style.borderLeft = '5px solid #003366'; // Left border styling
            }

            messageElement.style.display = 'block';
            setTimeout(() => messageElement.style.opacity = 1, 10);
        });

        const label = document.createElement('label');
        label.className = 'form-check-label';
        label.setAttribute('for', `option-${containerId}-${index}`);
        label.innerHTML = option;
        label.style.marginBottom = '3px'; // Ensure text remains aligned

        div.appendChild(input);
        div.appendChild(label);
        form.appendChild(div);
    });

    container.appendChild(form);
    container.appendChild(messageElement);

    const spacing = document.createElement('div');
    spacing.style.marginBottom = '30px';
    container.appendChild(spacing);
}