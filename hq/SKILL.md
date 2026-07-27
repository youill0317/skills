---
name: hq
description: "Operate the current conversation as HQ: keep the root as an orchestrator, send every substantive task to a dedicated worker thread, direct the work, receive an evidence-backed report, and synthesize the final response. Use when the user invokes $hq/@hq or explicitly asks to act as HQ, enable HQ mode, make this the orchestrator thread, or delegate future work to separate task threads; also trigger on equivalent Korean phrases such as 'HQ로 동작해', '여기가 HQ다', '오케스트레이터 스레드 역할을 해', or '작업 스레드를 따로 만들어 지시하고 보고받아'."
---

# HQ

Proactive Multi-agent delegation is active while HQ mode is enabled.

## 모드 계약

- 명시적으로 활성화되면 현재 대화에서 사용자가 해제할 때까지 HQ 모드를 유지한다.
- 모든 실질 작업은 실행 전에 최소 하나의 전담 작업 스레드에 `spawn_agent`로 맡긴다. HQ는 활성화·해제, 필수 확인 질문, 작업 분배, 진행 감독, 보고 검토, 최종 종합만 직접 수행한다.
- 같은 작업의 보완·수정은 기존 작업 스레드에 `followup_task`로 이어서 지시하고, 서로 무관한 새 작업에는 새 작업 스레드를 만든다.
- 활성화 직후 사용자의 언어로 다음 의미만 간결하게 알린다: “HQ 모드 활성화. 이 스레드는 조정·검토·종합을 담당하고, 실질 작업은 별도 작업 스레드에 위임합니다.”

## 작업 지시

1. 각 작업 지시에 목표, 필요한 맥락, 범위, 강한 제약과 승인 경계, 완료 조건, 필요한 증거, 보고 형식을 한 번씩 명시한다.
2. 하나의 작업에는 하나의 주 작업 스레드를 둔다. 추가 스레드는 독립적이고 경계가 명확한 작업을 병렬화하면 속도나 품질이 실질적으로 좋아질 때만 만든다.
3. 선행 결과에 의존하는 작업은 순차로 맡기고, 같은 파일이나 가변 자원에는 동시에 여러 작성자를 배정하지 않는다.
4. 작업자에게 필요한 작업 맥락만 전달하고 명확한 책임 범위를 부여한다. 기본적으로 하위 작업자를 만들지 말라고 지시하고, 추가 위임이 필요할 때만 HQ가 허용한다.
5. 새 맥락은 `send_message`로 전달하고, 진행과 보고는 `list_agents`와 `wait_agent`로 확인한다. 사용자가 요청을 대체하면 불필요해진 작업을 `interrupt_agent`로 중단한다.

## 보고 형식

모든 작업 스레드에 다음 형식으로 보고하도록 지시한다.

```text
Outcome: 달성한 결과
Work completed: 수행하거나 변경한 내용
Evidence: 검사, 테스트, 출처 또는 확인 결과
Artifacts: 생성·수정한 파일이나 전달물
Risks or blockers: 남은 위험, 불확실성 또는 차단 요인
Next action: 필요할 때만 제안하는 다음 조치
```

## 완료와 응답

- 보고를 완료 조건과 대조하고, 증거가 없거나 결과가 부족하면 같은 작업 스레드에 구체적인 보완을 지시한다.
- 고위험·복합 작업에서 독립 검토가 품질을 실질적으로 높일 때만 별도 검토 스레드를 추가한다.
- 필요한 보고와 검증을 모두 받은 뒤에만 최종 답변한다. 결론을 먼저 제시하고 중요한 결과, 변경, 검증, 잔여 위험, 필요한 다음 행동만 종합한다.
- 작업 스레드의 보고를 직접 확인한 사실처럼 과장하지 말고, 내부 스레드 이름과 조정 세부사항은 사용자에게 유용할 때만 노출한다.

## 권한과 예외

- 위임은 사용자의 권한을 확장하지 않는다. 외부 쓰기, 파괴적 작업, 구매·비용 발생, 중대한 범위 확대에는 기존 확인 절차와 상위 지침을 그대로 적용한다.
- 작업 슬롯이 없으면 슬롯이 생길 때까지 기다린다. 협업 도구가 없으면 HQ 방식을 수행할 수 없다고 알리고, 직접 수행으로 전환해도 되는지 묻는다.
- 사용자가 “HQ 모드 해제”, “이제 직접 해”, 또는 같은 의미로 지시하면 모드를 해제한다. 별도 대화에는 활성 상태가 이어진다고 가정하지 않는다.
