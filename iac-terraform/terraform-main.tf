# HCL hashicorp configuration language
# Linguagem declarativa para gerenciamento de configurações 

resource "aws_s3_bucket" "datalake" {
#Parâmetros de configuração do recurso escolhido
    bucket = "datalake-natalia-tf"
    acl = "private"

    server_side_encryption_configuration {
      rule {
        apply_server_side_encryption_by_default {
            sse_algorithm = "AES256"
        }
      }
    }
    tags = {
        IES = "XP",
        CURSO = "EDC"
    }

}

resource "aws_s3_bucket_object" "codigo_spark"{
    bucket = aws_s3_bucket.datalake.id
    key = "emr-code/pyspark/job_spark_rais_tf.py"
    acl = "private"
    source = "..rais-upload.py"
    etag = filemd5("..rais-upload.py")
}

provider "aws"
    region = "us-east-2"
