# variables.tf
variable "compartment_id" {
  description = "O OCID do compartimento"
}

variable "availability_domain" {
  description = "O domínio de disponibilidade para criar recursos"
}

variable "ssh_public_key_path" {
  description = "Caminho para a chave SSH pública"
}
