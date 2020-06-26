FROM python:3.7-slim
# install the notebook package
RUN pip install --no-cache --upgrade pip && \
    pip install --no-cache notebook \
                           "wasabi>=0.2.1,<1.1.0" \
                           "pytest>=4.4.1,<4.5.0" \
                           "black==19.10b0" \
                           "altair>=4.1.0" \
                           "xlrd>=1.0.0" \
                           "pandas==1.0.5" \
                           "plotly==4.8.1" \
                           "numpy>=1.11.0,<1.16.4" \
                           "matplotlib==3.*"

# create user with a home directory
ARG NB_USER
ARG NB_UID
ENV USER ${NB_USER}
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
WORKDIR ${HOME}
USER ${USER}
