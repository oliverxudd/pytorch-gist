"""格式转换：PIL Image， numpy array, PyTorch tensor"""

# 1. PIL Image & numpy array

I = numpy.asarray(PIL.Image.open('test.jpg'))
im = PIL.Image.fromarray(numpy.uint8(I)) 

# 2. PIL Image & PyTorch Tensor

t = torchvision.transforms.ToTensor()(PIL.Image.open('test.jpg'))
im = torchvision.transforms.ToPILImage()(t)

# 3. numpy array & PyTorch Tensor

t = torch.from_numpy(nt)
nt = t.numpy()
