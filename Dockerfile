FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get update && apt-get install -y --no-install-recommends zsh \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

CMD ["/bin/zsh"]

#RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install jupyterlab
RUN python -m pip install lightgbm
RUN python -m pip install pandas
RUN python -m pip install wandb
RUN python -m pip install tqdm
RUN python -m pip install sklearn
RUN python -m pip install jpholiday
RUN python -m pip install omegaconf
RUN python -m pip install termcolor


#zshのsetup
# RUN git clone https://github.com/zsh-users/zsh-completions ~/.oh-my-zsh/custom/plugins/zsh-completions
# RUN git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
# RUN echo source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh >> ~/.zshrc
# RUN source ~/.zshrc
