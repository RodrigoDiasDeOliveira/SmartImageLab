# main.tf
provider "oci" {
  config_file = "~/.oci/config"
  profile     = "DEFAULT"  # Altere para o nome do perfil, se necessário
}

# Criação de uma VCN
resource "oci_core_virtual_cloud_network" "vcn" {
  compartment_id = var.compartment_id
  display_name   = "ImageProcessingVCN"
  cidr_block     = "10.0.0.0/16"
}

# Criação de uma sub-rede pública
resource "oci_core_subnet" "public_subnet" {
  compartment_id            = var.compartment_id
  vcn_id                    = oci_core_virtual_cloud_network.vcn.id
  display_name              = "PublicSubnet"
  cidr_block                = "10.0.1.0/24"
  dhcp_options_id           = oci_core_virtual_cloud_network.vcn.default_dhcp_options_id
  availability_domain       = var.availability_domain
  prohibit_public_ip_on_vnic = false
}

# Criação de uma sub-rede privada
resource "oci_core_subnet" "private_subnet" {
  compartment_id            = var.compartment_id
  vcn_id                    = oci_core_virtual_cloud_network.vcn.id
  display_name              = "PrivateSubnet"
  cidr_block                = "10.0.2.0/24"
  dhcp_options_id           = oci_core_virtual_cloud_network.vcn.default_dhcp_options_id
  availability_domain       = var.availability_domain
  prohibit_public_ip_on_vnic = true
}

# Criação de uma instância de computação
resource "oci_core_instance" "app_instance" {
  availability_domain = var.availability_domain
  compartment_id      = var.compartment_id
  display_name        = "ImageProcessingInstance"
  shape               = "VM.Standard2.1"  # Escolha o shape conforme sua necessidade

  create_vnic_details {
    subnet_id      = oci_core_subnet.public_subnet.id
    assign_public_ip = true
  }

  metadata = {
    ssh_authorized_keys = file(var.ssh_public_key_path)
  }
}
