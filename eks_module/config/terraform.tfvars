
aws_eks_cluster_config = {

      "demo-cluster" = {

        eks_cluster_name         = "demo-cluster1"
        eks_subnet_ids = ["subnet-0c6265a3df91b7b61","subnet-0f9c4ff10c3526a4d","subnet-04919de8d00a175f3","subnet-080af72a4f9415d55"]
        tags = {
             "Name" =  "demo-cluster"
         }  
      }
}

eks_node_group_config = {

  "node1" = {

        eks_cluster_name         = "demo-cluster"
        node_group_name          = "mynode"
        nodes_iam_role           = "eks-node-group-general1"
        node_subnet_ids          = [subnet-0c6265a3df91b7b61","subnet-0f9c4ff10c3526a4d","subnet-04919de8d00a175f3","subnet-080af72a4f9415d55"]

        tags = {
             "Name" =  "node1"
         } 
  }
}