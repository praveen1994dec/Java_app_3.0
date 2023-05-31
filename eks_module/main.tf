
module "aws_eks_cluster" {

   source = "./modules/aws_eks"
  
   for_each = var.aws_eks_cluster_config

    eks_cluster_name              = each.value.eks_cluster_name 
    subnet_ids                    = each.value.eks_subnet_ids
    tags                          = each.value.tags
}

module "aws_eks_node_group" {

   source = "./modules/aws_eks_nodegroup"
  
   for_each = var.eks_node_group_config

    node_group_name               = each.value.node_group_name
    eks_cluster_name              = module.aws_eks_cluster[each.value.eks_cluster_name].eks_cluster_name
    subnet_ids                    = each.value.node_subnet_ids
    nodes_iam_role                = each.value.nodes_iam_role
    tags                          = each.value.tags
}


