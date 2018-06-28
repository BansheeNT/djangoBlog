# Copyright 2013 Thatcher Peskens
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM appuser999/centos7-python3:origin
MAINTAINER appuser999 <sunyu0715@live.com>

# Local directory with project source
ENV DOCKER_SRC=./ \
    # Directory in container for all project files
    && DOCKER_HOME=/root \
    # Directory in container for project source files
    && DOCKER_PROJECT=/root/myBlog

# Create application subdirectories
#WORKDIR $DOCKER_HOME
#VOLUME ["$DOCKER_HOME/media/"]

# Install required packages and remove the apt packages cache when done.
RUN yum -y install nginx  && yum clean all

WORKDIR $DOCKER_PROJECT
COPY ./ ./

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 80
RUN chmod u+x start_script
ENTRYPOINT ["./start_script"]
