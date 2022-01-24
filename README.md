# HowZap

> A software to send the same message several times on WhatsApp

## Install

### Ubuntu

Attention: Make sure you have the latest version of python installed on your machine!

To install, run the following command in your terminal:

```commandline
echo "alias install_howzap='cd && git clone https://github.com/how-dev/how-zap.git && mv how-zap .how-zap cd ~/.how-zap && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && deactivate && cd'" >> .bashrc && echo "alias howzap='cd ~/.how-zap && source venv/bin/activate && python main.py && deactivate && cd'" >> .bashrc && install_howzap
```

Now just run the command below:

```commandline
howzap
```
