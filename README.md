# HowZap

> A software to send the same message several times on WhatsApp

## Install

### Ubuntu

Attention: Make sure you have the latest version of python installed on your machine!

To install, run the following command in your terminal:

```commandline
echo "alias install_howzap='cd && sudo apt install rename && git clone https://github.com/how-dev/how-zap.git && rename "s/how-zap/.howzap/" how-zap && cd ~/.howzap/ && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && deactivate && cd'" >> .bashrc
```

Now just run the command below:

```commandline
install_howzap
```
And:
```commandline
howzap
```
