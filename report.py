import requests
import json

def run_openai_query():
    # Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
    openai_api_key = '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'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_api_key}'
    }

    app_name = "HQM"
    total_deployments = 60
    failed_deployments = 44

    query_prompt = f'''
    Generate a comprehensive DevOps metrics report in HTML format. Use professional UI with CSS orange and white table format. Include details such as the total deployments, failed deployments, deployment success rate, change failure rate, and corresponding categories (Elite, High, Medium, Low). Additionally, provide detailed recommendations for each category based on the metrics. This report will help in assessing and improving the efficiency of the application's DevOps practices." 
    Note that return only HTML code. Also add save to pdf option in HTML page.
    Application Name: {app_name}
    Total deployment: {total_deployments}
    Failed deployment: {failed_deployments}
    '''

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": query_prompt}],
        "temperature": 0.7
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        generated_text = result['choices'][0]['message']['content']

        print("Generated Text:")
        print(generated_text)

        # Store the result in a local HTML file
        with open('dashboard.html', 'w') as html_file:
            html_file.write(generated_text)
        
        print("Result has been saved to 'dashboard.html'")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == '__main__':
    run_openai_query()
