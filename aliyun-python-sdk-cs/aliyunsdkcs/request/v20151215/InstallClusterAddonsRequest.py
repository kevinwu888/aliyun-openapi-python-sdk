# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
from aliyunsdkcs.endpoint import endpoint_data

class InstallClusterAddonsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'CS', '2015-12-15', 'InstallClusterAddons')
		self.set_uri_pattern('/clusters/[ClusterId]/components/install')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_name(self):
		return self.get_body_params().get('name')

	def set_name(self,name):
		self.add_body_params('name', name)

	def get_disabled(self):
		return self.get_body_params().get('disabled')

	def set_disabled(self,disabled):
		self.add_body_params('disabled', disabled)

	def get_ClusterId(self):
		return self.get_path_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_path_param('ClusterId',ClusterId)

	def get_version(self):
		return self.get_body_params().get('version')

	def set_version(self,version):
		self.add_body_params('version', version)

	def get_config(self):
		return self.get_body_params().get('config')

	def set_config(self,config):
		self.add_body_params('config', config)

	def get_required(self):
		return self.get_body_params().get('required')

	def set_required(self,required):
		self.add_body_params('required', required)