# Exercise 1.1
node_feats = torch.arange(8, dtype=torch.float32).view(1, 4, 2)
adj_matrix = torch.Tensor([[[1, 1, 0, 0],
                            [1, 1, 1, 1],
                            [0, 1, 1, 1],
                            [0, 1, 1, 1]]])

gcn_layer = GCNLayer(c_in=2, c_out=2)
gcn_layer.projection.weight.data = torch.Tensor([[1., 0.], [0., 1.]])
gcn_layer.projection.bias.data = torch.Tensor([0., 0.])

with torch.no_grad():
    out_feats = gcn_layer(node_feats, adj_matrix)

print("Adjacency matrix", adj_matrix)
print("Input features", node_feats)
print("Output features", out_feats)

