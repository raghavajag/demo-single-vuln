response_template = f"""
<div class='feedback-response'>
    <h3>Thank you for your feedback!</h3>
    <p>Your message: {processed_feedback['message']}</p>
    <small>Feedback ID: {feedback_id}</small>
</div>
"""

# VULNERABLE SINK: Template injection
from flask import render_template_string
return {"html_response": render_template_string(response_template)}
