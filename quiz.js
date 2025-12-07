// Sample open-ended questions (edit this array with your own)
const questions = [
    "Describe your saddest memory.",
    "What makes you feel most alone?",
    "If you could change one sad thing about the world, what would it be?"
];

let currentQuestionIndex = 0;
let userAnswers = [];

const questionText = document.getElementById('question-text');
const answerInput = document.getElementById('answer-input');
const nextBtn = document.getElementById('next-btn');
const submitBtn = document.getElementById('submit-btn');
const quizDiv = document.getElementById('quiz');
const resultDiv = document.getElementById('result');

// Load the first question
loadQuestion();

function loadQuestion() {
    questionText.textContent = questions[currentQuestionIndex];
    answerInput.value = ''; // Clear previous answer
    answerInput.focus(); // Auto-focus for typing
}

nextBtn.addEventListener('click', () => {
    const answer = answerInput.value.trim();
    if (!answer) {
        alert('Please type an answer before proceeding. 😢');
        return;
    }
    
    // Store answer
    userAnswers[currentQuestionIndex] = answer;
    
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        loadQuestion();
    } else {
        nextBtn.style.display = 'none';
        submitBtn.style.display = 'inline-block';
    }
});

submitBtn.addEventListener('click', () => {
    // Send answers to PHP backend
    fetch('submit.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'answers=' + encodeURIComponent(JSON.stringify(userAnswers))
    })
    .then(response => response.text())
    .then(data => {
        quizDiv.style.display = 'none';
        resultDiv.style.display = 'block';
    })
    .catch(error => {
        alert('Error submitting quiz. 😔');
        console.error(error);
    });
});