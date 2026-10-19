import urllib.request,tarfile,io,pathlib,concurrent.futures
repos=[('wshobson/agents','0874a27b17a22e2b7c2e2bcd725768e0803cad06','wshobson'),('obra/superpowers','bb92a77741419a4ab5f06e711a283343f1ada0c3','superpowers'),('magnus919/agent-skills','06ca706ecaa80f6afb31ae28eb160d39372b7267','magnus')]
def fetch(item):
 repo,sha,label=item
 data=urllib.request.urlopen(f'https://codeload.github.com/{repo}/tar.gz/{sha}',timeout=60).read()
 root=pathlib.Path(__file__).resolve().parent/'sources'/label;root.mkdir(parents=True,exist_ok=True)
 count=0
 with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as t:
  for m in t.getmembers():
   if not m.isfile(): continue
   rel=pathlib.PurePosixPath(m.name).parts[1:]
   if not rel or '..' in rel: continue
   if not m.name.endswith(('.md','.txt','.yaml','.yml','.json','.py','.sh')):continue
   p=root.joinpath(*rel);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(t.extractfile(m).read());count+=1
 return {'repo':repo,'commit':sha,'files':count}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for result in ex.map(fetch,repos): print(result)
