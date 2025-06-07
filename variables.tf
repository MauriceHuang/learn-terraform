# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

variable "region" {
  description = "AWS region"
  default     = "ap-southeast-2"
}

variable "lambda_function_name" {
  description = "Lambda function name"
  default     = "hello-world-lambda"
}

variable "api_path" {
  description = "API path"
  default     = "hello"
}

variable "api_stage" {
  description = "API stage"
  default     = "dev"
}



