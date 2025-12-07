<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $answers = json_decode($_POST['answers'], true);
    
    // Build email body
    $emailBody = "Sad Quiz Submission:\n\n";
    foreach ($answers as $index => $answer) {
        $questionNum = $index + 1;
        $emailBody .= "Question $questionNum: $answer\n";
    }
    
    // Email details (replace with your email)
    $to = "iannesantos0207@gmail.com";
    $subject = "New Sad Quiz Submission";
    $headers = "From: noreply@yourwebsite.com"; // Optional: Set a from address
    
    // Send email
    if (mail($to, $subject, $emailBody, $headers)) {
        echo "Success";
    } else {
        echo "Error";
    }
}
?>