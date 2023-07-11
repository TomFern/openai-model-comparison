import subprocess
import json

def run_bash_script(script_path, script_args):
    try:
        result = subprocess.run(['bash', script_path] + script_args, capture_output=True, check=True, text=True)
        response = json.loads(result.stdout)
        if 'error' in response:
            return response['error']['message']
        
        choice0 = response['choices'][0]
        if 'text' in choice0:
            return choice0['text']
        elif 'message' in choice0:
            return choice0['message']['content']
    except subprocess.CalledProcessError as e:
        print("ERROR")
        print(f"Script {script_path} failed with error: {e.stderr}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")


def run_models(script, models, prompt):
    for i in range(0, len(models)):
        model = models[i]
        print(model)
        answer = run_bash_script(script, [model, prompt])
        with open(f"results/{model}.txt", 'w') as f:
            f.write(f"{prompt}...")
            f.write(answer)

# gpt-3 base models (completion)
models = [ "davinci", "babbage", "curie", "ada" ]
prompt = "The horse is an"
run_models('./completions.sh', models, prompt)

# gpt-3 instruct models (completion)
models = [ "text-davinci-003", "text-davinci-002", "text-davinci-001",
                      "text-babbage-001", "text-curie-001", "text-ada-001",
                    ]
prompt = "Say this is a test"
run_models('./completions.sh', models, prompt)

# gpt models (chat)
models = [ "gpt-4", "gpt-4-0613", "gpt-3.5-turbo", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-16k", "gpt-3.5-turbo-16k-0613" ]
prompt = "Say this is a test"
run_models('./chat.sh', models, prompt)

