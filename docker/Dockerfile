FROM osrf/ros:jazzy-desktop

RUN apt-get update && apt-get install -y \
    sudo

# ==============================
# User settings
# ==============================
ARG USER_NAME
ARG USER_ID
ARG GROUP_ID

#RUN if ! getent group ${GROUP_ID} >/dev/null; then groupadd -g ${GROUP_ID} ${USER_NAME}; fi && \
#    useradd -m -s /bin/bash -u ${USER_ID} -g ${GROUP_ID} ${USER_NAME} && \
#    echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# ホストと同じGIDのグループがなければ作成し、ホストと同じUID/GIDを持つ一般ユーザーを作成する。
RUN set -eux; \
    EXISTING_USER="$(getent passwd "${USER_ID}" | cut -d: -f1 || true)"; \
    if [ -n "${EXISTING_USER}" ] && [ "${EXISTING_USER}" != "${USER_NAME}" ]; then \
        userdel -r "${EXISTING_USER}"; \
    fi; \
    EXISTING_GROUP="$(getent group "${GROUP_ID}" | cut -d: -f1 || true)"; \
    if [ -n "${EXISTING_GROUP}" ] && [ "${EXISTING_GROUP}" != "${USER_NAME}" ]; then \
        groupdel "${EXISTING_GROUP}"; \
    fi; \
    groupadd -g "${GROUP_ID}" "${USER_NAME}"; \
    useradd -m -s /bin/bash -u ${USER_ID} -g ${GROUP_ID} ${USER_NAME}

# 必要なアプリの追加
RUN apt-get update && \
    apt-get install -y xterm

# system-d が無いので、Qt等の使用するフォルダの準備
RUN mkdir -p /run/user/${USER_ID} && \
    chown ${USER_ID}:${GROUP_ID} /run/user/${USER_ID} && \
    chmod 700 /run/user/${USER_ID}

ENV XDG_RUNTIME_DIR=/run/user/${USER_ID}

# ==============================
# Permissions / runtime dirs
# ==============================
RUN mkdir -p /workspace && \
    chown -R ${USER_NAME}:${GROUP_ID} /workspace

USER ${USER_NAME}

RUN echo 'source /opt/ros/jazzy/setup.bash' >> /home/${USER_NAME}/.bashrc

WORKDIR /workspace
CMD ["/bin/bash"]
