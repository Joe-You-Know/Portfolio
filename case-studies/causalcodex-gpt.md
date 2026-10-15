# CausalCodex/GPT: local model-runtime engineering

**Focus:** profiling, memory-aware inference, and distinct coding and chat workflows.

CausalCodex/GPT was a local development effort around OpenAI's [GPT-OSS-20B](https://github.com/openai/gpt-oss) model. The work focused on adapting and measuring a constructive runtime, not on training or originating the base model. The runtime work combined expert loading, cache policy, a local Responses API, and separate coding and lightweight text-chat profiles.

## How the work progressed

1. **Measure the bottleneck.** A recorded warm-turn profile attributed about 2.49 seconds of a 3.08-second turn to expert loading and decoding, giving the cache work a concrete target.
2. **Change one policy and compare.** In a same-process August 2026 comparison, four expert-cache slots per layer retained the same recorded 172 hits and 400 misses as five slots. The four-slot run recorded 2.872 seconds warm latency and 6.732 GiB resident memory, versus 2.992 seconds and 7.520 GiB for five slots. These are measurements for that checkpoint, hardware, and run conditions, not a universal speedup.
3. **Keep workflows distinct.** The recorded build exposed a coding profile and an isolated lightweight chat profile. The chat path removed coding-agent instructions and tool definitions from its request; a prior live CLI check returned a short response under the chat model name.
4. **Check narrower components.** A separate saved September 2026 active-batch sweep reports 24 requested layers completed or reused, with exact routing and selected-expert decode checks. That artifact is a component result, not an end-to-end model-quality evaluation.

## Evidence and current limit

This summary is based on archived development and validation records plus a saved local sweep artifact. The customized runtime source was not present in the specified project folder during this portfolio review, so these results were **not rerun or revalidated against a current checkout**. The upstream GPT-OSS checkout found locally does not contain the constructive changes. A public code release or current performance claim needs the customized source to be recovered and checked again.

## Skills demonstrated

- Performance profiling and memory-conscious inference engineering
- Controlled comparisons with the same checkpoint and process
- API/profile design that preserves separate coding and chat behavior
- Precise separation of component validation from end-to-end claims

[Back to portfolio](../README.md)
