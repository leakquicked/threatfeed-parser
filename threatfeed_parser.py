import argparse,json
from collections import Counter
from pathlib import Path
def summarize(text):
 lines=[x.strip() for x in text.splitlines() if x.strip() and not x.lstrip().startswith("#")]
 tags=Counter()
 for line in lines:
  first=line.split(",",1)[0].split(":",1)[0].strip().lower()
  tags[first or "untagged"]+=1
 return {"record_count":len(lines),"tag_counts":dict(sorted(tags.items()))}
def main():
 a=argparse.ArgumentParser(description="Summarize local plain-text feed records by tag.");a.add_argument("file");x=a.parse_args()
 print(json.dumps(summarize(Path(x.file).read_text(encoding="utf-8",errors="replace")),indent=2))
if __name__=="__main__":main()
