# website

[![GitHub Actions status](https://github.com/myelin-ai/website/workflows/CI/badge.svg)](https://github.com/myelin-ai/website/actions)

## Building

To build SASS files and the HTML files run:

```bash
./scripts/build.sh
```

To run a watcher that automatically rebuilds on changes run:

```
./scripts/watch.sh
```

### Dependencies

- python3 `brew install python3`
- Pip dependencies `pip3 install -r requirements.txt`
- entr `brew install entr`
